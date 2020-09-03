#version 330 core
layout (points) in;
layout (triangle_strip, max_vertices = 4) out;

in vec2 v_radius[];
in vec4 v_color[];

uniform mat4x4 u_projection;

out vec2 vf_uv;
out vec4 vf_color;
out float vf_solid_factor;

void ProcessVert(vec2 offset)
{
    vec2 posWorldSpace = gl_in[0].gl_Position.xy + offset * v_radius[0].y;

    vec4 finalPositionWorldSpace = vec4(posWorldSpace, 0.0, 1.0);//Expand to vec4 for matrix multiplication
    vec4 finalPositionClipSpace = u_projection * finalPositionWorldSpace; //Multiply by projection matrix to take camera position and zoom into account

    gl_Position = finalPositionClipSpace;
    vf_uv = offset;//Pass offset as UV like value to fragment shader
    vf_color = v_color[0];//Pass color to fragment shader
    vf_solid_factor = v_radius[0].x / v_radius[0].y;
    EmitVertex();
}

void main() 
{
    //By calling this method 4 times, we expand a single point into 4 verts that form a quad based on the particle radius
    ProcessVert(vec2(-1.0, -1.0));
    ProcessVert(vec2(-1.0, 1.0));
    ProcessVert(vec2(1.0, -1.0));
    ProcessVert(vec2(1.0, 1.0));
    EndPrimitive();
}  