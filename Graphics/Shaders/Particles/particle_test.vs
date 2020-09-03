#version 330

// (x, y) position passed in
in vec2 in_pos;
in vec2 in_radius;
in vec4 in_color;
in vec2 in_vel;
// Output the distance from the fragment(manhatton taxi) to the center of the light
out vec2 v_radius;
out vec4 v_color;

uniform float u_time;

void main() {

    v_radius = in_radius;
    v_color = in_color;

    vec2 finalPos = in_pos;

    // Set the position. (x, y, z, w)
    gl_Position = vec4(finalPos, 0.0, 1);//Kept in world space, geomtetry shader will mul by projection after radius expansion to qud
}