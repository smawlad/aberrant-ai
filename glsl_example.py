import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

# Vertex shader
vertex_shader = """
#version 330 core
in vec2 position;
void main() {
    gl_Position = vec4(position, 0.0, 1.0);
}
"""

# Fragment shader
fragment_shader = """
#version 330 core
out vec4 fragColor;
void main() {
    fragColor = vec4(1.0, 0.0, 0.0, 1.0);  // Red color
}
"""

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Compile shaders
    shader = compileProgram(
        compileShader(vertex_shader, GL_VERTEX_SHADER),
        compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    )

    # Create a square
    vertices = [
        -0.5, -0.5,
         0.5, -0.5,
         0.5,  0.5,
        -0.5,  0.5
    ]

    # Vertex Buffer Object
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, len(vertices) * 4, (GLfloat * len(vertices))(*vertices), GL_STATIC_DRAW)

    # Use the shader program
    glUseProgram(shader)

    # Get the position attribute location
    position = glGetAttribLocation(shader, "position")
    glEnableVertexAttribArray(position)
    glVertexAttribPointer(position, 2, GL_FLOAT, GL_FALSE, 0, None)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glDrawArrays(GL_TRIANGLE_FAN, 0, 4)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
