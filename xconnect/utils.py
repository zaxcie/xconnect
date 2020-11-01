from datetime import datetime

def save_env_render_html(html: str):
    '''
    Save an env.render html page to the reports folder. The name of the file always contain the datetime of the run.
    '''
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")

    with open(f"reports/run_{dt_string}.html", "w") as file:
        file.write(html)
