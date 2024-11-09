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
    # проверка нажатия
    # pyray предоставляет несколько разных способов обновления нажатия, поэкспериментируйте с ними(pr.is_key_pressed, pr.is_key_down, pr.is_key_up)
    # ось x
    if pr.is_key_pressed(pr.KeyboardKey.KEY_LEFT):
        pos[0] -= 0.1
    if pr.is_key_pressed(pr.KeyboardKey.KEY_RIGHT):
        pos[0] += 0.1
    # ось z
    if pr.is_key_pressed(pr.KeyboardKey.KEY_UP):
        pos[2] -= 0.1
    if pr.is_key_pressed(pr.KeyboardKey.KEY_DOWN):
        pos[2] += 0.1

    # обновление камеры и ее режима
    # режимы хранятся в енуме pr.Cameramode, попробуйте поэкспериментировать с ним
    # pr.update_camera(camera, pr.CameraMode.CAMERA_THIRD_PERSON)

    # начало отрисовки
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)  # заливка фона белым цветом

    # ! переход в режим 3д для отрисовки трехмерных объектов
    pr.begin_mode_3d(camera)
    pr.draw_grid(20, 1)  # сетка с 20 делениями длиной в 1 юнит
    pr.draw_cube(
        pos, 1, 1, 1, pr.PURPLE
    )  # отрисовка фиолетового куба объемом 1 в центрее
    pr.end_mode_3d()  # !!! когда закончили отрисовывать трехмерные объекты, возвращаемся обратно в режим 2д

    pr.draw_text("woah", 100, 150, 25, pr.GREEN)  # отрисовываем текст(2д объект!)
    pr.end_drawing()  # заканчиваем отрисовку

pr.close_window()  # закрытие окна