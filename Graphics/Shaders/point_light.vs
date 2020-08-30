#version 330

// (x, y) position passed in
in vec2 in_pos;
in vec2 in_uv;

uniform vec2 u_position;
uniform float u_radius;

uniform mat4x4 u_projection;

// Output the distance from the fragment(manhatton taxi) to the center of the light
out vec2 v_distance;

void main() {

    //Scale input quad by the radius of the light
    vec4 finalPos = vec4(in_pos * u_radius, 0.0, 1.0);

    //translate by position
    finalPos.xy += u_position;

    //apply camera projection matrix
    finalPos = u_projection * finalPos;


    //convert uv to -1 -> 1 range and multiply UV by radius to get a simple distance computation in 
    //the fragment shader, but in world space to as to ignore effects of camera zoom/camera dims
    v_distance = (in_uv - 0.5) * 2.0 * u_radius;

    // Set the position. (x, y, z, w)
    gl_Position = vec4(finalPos.xy, 0.0, 1);
}