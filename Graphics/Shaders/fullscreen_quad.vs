#version 330

// (x, y) position passed in
in vec2 in_pos;
in vec2 in_uv;

// Output the color to the fragment shader
out vec2 v_uv;

void main() {

    // Pass UV though to be interpolated
    v_uv = in_uv;

    // Set the position. (x, y, z, w)
    gl_Position = vec4(in_pos, 0.0, 1);
}