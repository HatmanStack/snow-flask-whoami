"""Flask application factory for snow-flask-whoami."""
from typing import Union, Tuple, Optional
import json
import logging

from flask import Flask, render_template, request

from snow_flask_core.database import get_db
from snow_flask_core.validation import validate_name, validate_address, ValidationError
from snow_flask_core.models import ChartData

logger = logging.getLogger(__name__)


def create_app(
    template_folder: Optional[str] = None,
    static_folder: Optional[str] = None
) -> Flask:
    """Create and configure the Flask application.

    Args:
        template_folder: Optional custom template folder path.
        static_folder: Optional custom static folder path.

    Returns:
        Configured Flask application.
    """
    kwargs = {}
    if template_folder:
        kwargs['template_folder'] = template_folder
    if static_folder:
        kwargs['static_folder'] = static_folder

    app = Flask(__name__, **kwargs)

    @app.route('/')
    def homepage() -> Union[str, Tuple[str, int]]:
        """Render the homepage with chart data."""
        try:
            with get_db().cursor() as cur:
                cur.execute("SELECT Name, count(*) FROM ADDRESSES GROUP BY NAME")
                chart_data: ChartData = [
                    {'NAME': row[0], 'vote': row[1]} for row in cur.fetchall()
                ]
                data4chartsJSON = json.dumps(chart_data)

            with get_db().cursor() as cur:
                cur.execute("SELECT ADDRESS, NAME FROM ADDRESSES LIMIT 50")
                threejs_stream_data = json.dumps(cur.fetchall())

            return render_template(
                'charts.html',
                data4chartsJSON=data4chartsJSON,
                threejs_stream_data=threejs_stream_data
            )
        except Exception:
            logger.error("Failed to load homepage", exc_info=True)
            return render_template(
                'error.html',
                error_title="Error",
                error_message="Failed to load data"
            ), 500

    @app.route('/Submit')
    def submitpage() -> str:
        """Render the submission form."""
        return render_template('submit.html')

    @app.route('/HardData')
    def hard_data() -> Union[str, Tuple[str, int]]:
        """Render the interactive data visualization with pagination."""
        try:
            limit = min(request.args.get('limit', 100, type=int), 500)
            offset = request.args.get('offset', 0, type=int)

            with get_db().cursor() as cur:
                cur.execute(
                    "SELECT ADDRESS, NAME FROM ADDRESSES LIMIT %s OFFSET %s",
                    (limit, offset)
                )
                interactive_table_data = json.dumps(cur.fetchall())

            return render_template('index.html', interactive_table_data=interactive_table_data)
        except Exception:
            logger.error("Failed to load data", exc_info=True)
            return render_template(
                'error.html',
                error_title="Error",
                error_message="Failed to load data"
            ), 500

    @app.route('/thanks4submit', methods=["POST"])
    def thanks4submit() -> Union[str, Tuple[str, int]]:
        """Handle form submission."""
        try:
            address = validate_address(request.form.get("cname"))
            name = validate_name(request.form.get("uname"))

            with get_db().cursor() as cur:
                cur.execute(
                    "INSERT INTO ADDRESSES(ADDRESS, NAME) VALUES (%s, %s)",
                    (address, name)
                )

            logger.info("Address submitted", extra={'name_length': len(name)})
            return render_template(
                'thanks4submit.html',
                colorname=address,
                username=name
            )
        except ValidationError as e:
            return render_template(
                'error.html',
                error_title="Invalid Input",
                error_message=str(e)
            ), 400
        except Exception:
            logger.error("Submission failed", exc_info=True)
            return render_template(
                'error.html',
                error_title="Error",
                error_message="Submission failed"
            ), 500

    return app
