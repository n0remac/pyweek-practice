#version 330

// (x, y) position passed in
//Declare in's to make shader line up. IGNORE THEM
in vec2 in_pos;
in vec2 in_radius;
in vec4 in_color;
in vec2 in_vel;


// Output the distance from the fragment(manhatton taxi) to the center of the light
out vec2 out_pos;
out vec2 out_radius;
out vec2 out_vel;
out vec4 out_color;

uniform vec2 u_burst_point;
uniform vec2 u_burst_power;

float random (in vec2 st) {
    return fract(sin(dot(st.xy,
                         vec2(12.3218,78.233)))
                 * 43758.5453123);
}

void main() 
{

    vec2 burstDir;
    burstDir.x = random(vec2(gl_VertexID / 256.0, gl_VertexID/1003)) - 0.5;
    burstDir.y = random(vec2(gl_VertexID /256.0, gl_VertexID/2.14)) - 0.5;

    burstDir = normalize(burstDir);

    float otherRand = random(vec2(gl_VertexID/ 2.1, gl_VertexID/3.4));

    vec2 finalVel = burstDir * mix(u_burst_power.x, u_burst_power.y, otherRand);

    out_pos = u_burst_point;
    out_vel = finalVel;


    out_radius = in_radius;
    out_color = in_color;
}