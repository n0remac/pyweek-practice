#version 330

// (x, y) position passed in
in vec2 in_pos;
in vec2 in_radius;
in vec4 in_color;
in vec2 in_vel;
// Output the distance from the fragment(manhatton taxi) to the center of the light
out vec2 out_pos;
out vec2 out_radius;
out vec2 out_vel;
out vec4 out_color;

uniform float u_delta_time;
uniform vec2 u_gravity;
uniform float u_drag;

uniform vec2 u_mouse_pos;
uniform float u_mouse_power;

void main() 
{


    vec2 finalVel = in_vel + u_gravity * u_delta_time;

    vec2 toMouse = u_mouse_pos - in_pos;

    float dist = length(toMouse);
    toMouse = toMouse / dist;

    if(dist <= 0.001 || isnan(dist)){
        dist = 100000.0;
        toMouse = vec2(0.0);
    }

    dist /= 1000.0;

    float mouseFalloff = u_mouse_power / (dist*dist);

    finalVel = finalVel * u_drag;
    finalVel += toMouse * u_delta_time * mouseFalloff;

    out_pos = in_pos + finalVel * u_delta_time;
    out_radius = in_radius;
    out_vel = finalVel;
    out_color = in_color;
}