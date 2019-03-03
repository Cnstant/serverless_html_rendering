import time

import numpy as np
from flask import Flask, render_template

# App config.
DEBUG = True
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def html5_rendering():
    seed = 723
    timestamp = int(time.time())

    # Random choice
    np.random.seed(seed)
    text = {'gradient_0_x': np.random.randint(50, 150), 'gradient_0_y': np.random.randint(50, 150),
            'gradient_r_0': np.random.randint(50, 150),
            'gradient_1_x': np.random.randint(50, 150), 'gradient_1_y': np.random.randint(50, 150),
            'gradient_r_1': np.random.randint(50, 150),
            'starting_color_r': np.random.randint(0, 255), 'starting_color_g': np.random.randint(0, 255),
            'starting_color_b': np.random.randint(0, 255), 'starting_color_transparency': round(np.random.rand(), 1),
            'end_color_r': np.random.randint(0, 255), 'end_color_g': np.random.randint(0, 255),
            'end_color_b': np.random.randint(0, 255), 'end_color_transparency': round(np.random.rand(), 1),
            'shadow_color_r': np.random.randint(0, 255), 'shadow_color_g': np.random.randint(0, 255),
            'shadow_color_b': np.random.randint(0, 255),
            'shadow_blur': np.random.randint(0, 100),

            'font_size': np.random.randint(5, 50),
            'fillText_start': np.random.randint(0, 100),
            'fillText_end': np.random.randint(100, 200),
            }

    arc = {'gradient_0_x': np.random.randint(50, 150), 'gradient_0_y': np.random.randint(50, 150),
           'gradient_r_0': np.random.randint(50, 150),
           'gradient_1_x': np.random.randint(50, 150), 'gradient_1_y': np.random.randint(50, 150),
           'gradient_r_1': np.random.randint(50, 150),
           'starting_color_r': np.random.randint(0, 255), 'starting_color_g': np.random.randint(0, 255),
           'starting_color_b': np.random.randint(0, 255), 'starting_color_transparency': round(np.random.rand(), 1),
           'end_color_r': np.random.randint(0, 255), 'end_color_g': np.random.randint(0, 255),
           'end_color_b': np.random.randint(0, 255), 'end_color_transparency': round(np.random.rand(), 1),
           'shadow_color_r': np.random.randint(0, 255), 'shadow_color_g': np.random.randint(0, 255),
           'shadow_color_b': np.random.randint(0, 255),
           'shadow_blur': np.random.randint(0, 100),

           'start_x': np.random.randint(50, 150), 'start_y': np.random.randint(50, 150),
           'radius': np.random.randint(0, 100),
           'angle_start': 2 * round(np.random.rand(), 2), 'angle_end': 2 * round(np.random.rand(), 2)
           }

    bezier = {'gradient_0_x': np.random.randint(50, 150), 'gradient_0_y': np.random.randint(50, 150),
              'gradient_r_0': np.random.randint(50, 150),
              'gradient_1_x': np.random.randint(50, 150), 'gradient_1_y': np.random.randint(50, 150),
              'gradient_r_1': np.random.randint(50, 150),
              'starting_color_r': np.random.randint(0, 255), 'starting_color_g': np.random.randint(0, 255),
              'starting_color_b': np.random.randint(0, 255), 'starting_color_transparency': round(np.random.rand(), 1),
              'end_color_r': np.random.randint(0, 255), 'end_color_g': np.random.randint(0, 255),
              'end_color_b': np.random.randint(0, 255), 'end_color_transparency': round(np.random.rand(), 1),
              'shadow_color_r': np.random.randint(0, 255), 'shadow_color_g': np.random.randint(0, 255),
              'shadow_color_b': np.random.randint(0, 255),
              'shadow_blur': np.random.randint(0, 100),

              'start_x': np.random.randint(50, 150), 'start_y': np.random.randint(50, 150),
              'cp1x': np.random.randint(50, 150), 'cp1y': np.random.randint(50, 150),
              'cp2x': np.random.randint(50, 150), 'cp2y': np.random.randint(50, 150),
              'x': np.random.randint(50, 150), 'y': np.random.randint(50, 150)
              }

    quadratic = {'gradient_0_x': np.random.randint(50, 150), 'gradient_0_y': np.random.randint(50, 150),
                 'gradient_r_0': np.random.randint(50, 150),
                 'gradient_1_x': np.random.randint(50, 150), 'gradient_1_y': np.random.randint(50, 150),
                 'gradient_r_1': np.random.randint(50, 150),
                 'starting_color_r': np.random.randint(0, 255), 'starting_color_g': np.random.randint(0, 255),
                 'starting_color_b': np.random.randint(0, 255),
                 'starting_color_transparency': round(np.random.rand(), 1),
                 'end_color_r': np.random.randint(0, 255), 'end_color_g': np.random.randint(0, 255),
                 'end_color_b': np.random.randint(0, 255), 'end_color_transparency': round(np.random.rand(), 1),
                 'shadow_color_r': np.random.randint(0, 255), 'shadow_color_g': np.random.randint(0, 255),
                 'shadow_color_b': np.random.randint(0, 255),
                 'shadow_blur': np.random.randint(0, 100),

                 'start_x': np.random.randint(50, 150), 'start_y': np.random.randint(50, 150),
                 'cpx': np.random.randint(50, 150), 'cpy': np.random.randint(50, 150),
                 'x': np.random.randint(50, 150), 'y': np.random.randint(50, 150)
                 }

    return render_template('upload_canvas_to_S3.html',
                           seed=seed,
                           timestamp=timestamp,
                           text=text,
                           arc=arc,
                           bezier=bezier,
                           quadratic=quadratic)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
