import pyray as pr

# инициализация окна: его размеры, название и целевой фреймрейт
pr.init_window(800, 600, "welcome fanatics")
pr.set_target_fps(60)

# создание отдельной камеры с возможностью отрисовки в 3д
camera = pr.Camera3D(
    [6.0, 4.0, 9.0],
    [0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    45.0,
    pr.CameraProjection.CAMERA_PERSPECTIVE,
)

pos = [0, 0, 0]

# основной цикл - работает, пока не закроется окно
while not pr.window_should_close():
    # обновление камеры и ее режима
    # режимы хранятся в енуме pr.Cameramode, попробуйте поэкспериментировать с ним
    pr.update_camera(camera, pr.CameraMode.CAMERA_FREE)

    # начало отрисовки
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)  # заливка фона белым цветом

    # ! переход в режим 3д для отрисовки трехмерных объектов
    pr.begin_mode_3d(camera)
    pr.draw_grid(20, 1)  # сетка с 20 делениями длиной в 1 юнит

    # движение происходит по 3 осям x,y,z
    pr.draw_cylinder_ex([0, 0, 0], [3, 0, 0], 0.1, 0.1, 10, pr.RED)
    pr.draw_cylinder_ex([3, 0, 0], [3.5, 0, 0], 0.3, 0, 10, pr.RED)
    pr.draw_cylinder_ex([0, 0, 0], [0, 3, 0], 0.1, 0.1, 10, pr.BLUE)
    pr.draw_cylinder_ex([0, 3, 0], [0, 3.5, 0], 0.3, 0, 10, pr.BLUE)
    pr.draw_cylinder_ex([0, 0, 0], [0, 0, 3], 0.1, 0.1, 10, pr.GREEN)
    pr.draw_cylinder_ex([0, 0, 3], [0, 0, 3.5], 0.3, 0, 10, pr.GREEN)

    pr.end_mode_3d()  # !!! когда закончили отрисовывать трехмерные объекты, возвращаемся обратно в режим 2д

    pr.draw_text(
        "3d has 3 axis", 100, 150, 25, pr.GREEN
    )  # отрисовываем текст(2д объект!)
    pr.draw_text_ex(
        pr.get_font_default(),
        "X",
        pr.get_world_to_screen([3.8, 0, 0], camera),
        30,
        1,
        pr.RED,
    )
    pr.draw_text_ex(
        pr.get_font_default(),
        "Z",
        pr.get_world_to_screen([0, 3.8, 0], camera),
        30,
        1,
        pr.BLUE,
    )
    pr.draw_text_ex(
        pr.get_font_default(),
        "Y",
        pr.get_world_to_screen([0, 0, 3.8], camera),
        30,
        1,
        pr.GREEN,
    )
    pr.end_drawing()  # заканчиваем отрисовку

pr.close_window()  # закрытие окна
