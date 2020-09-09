#version 330

// Color passed in from the vertex shader
in vec2 v_uv;

// The pixel we are writing to in the framebuffer
out vec4 fragColor;

uniform sampler2D t_source; 
uniform sampler2D t_lut;

uniform float u_strength;


const float size = 16.0;

const float x_step = 1.0 / (size * size);
const float x_block = 1.0 / size;
const float y_step = 1.0 / size;

const vec2 half_voxel = vec2(x_step, y_step) * 0.5;


vec3 sample_x(float low, float high, float y, float z, float frac, sampler2D lut){

    vec3 sample_low = texture(lut, half_voxel + vec2(low+z, y)).rgb;
    vec3 sample_high = texture(lut, half_voxel + vec2(high+z, y)).rgb;

    return mix(sample_low, sample_high, frac);
}

vec3 sample_lut(vec3 color, sampler2D lut){

    vec3 scaled = color * 15.0;

    vec3 low = floor(scaled);
    vec3 high = ceil(scaled);
    vec3 frac = scaled - low;

    low.x *= x_step;
    high.x *= x_step;

    low.yz *= y_step;
    high.yz *= y_step;

    vec3 x00 = sample_x(low.x, high.x,      low.y, low.z,   frac.x,lut);
    vec3 x01 = sample_x(low.x, high.x,      low.y, high.z,   frac.x,lut);
    vec3 x10 = sample_x(low.x, high.x,      high.y, low.z,   frac.x,lut);
    vec3 x11 = sample_x(low.x, high.x,      high.y, high.z,   frac.x,lut);

    vec3 y0 = mix(x00, x01, frac.z);
    vec3 y1 = mix (x10, x11, frac.z);

    return mix(y0, y1, frac.y);
}


void main() {

    vec4 sourceColor = texture(t_source, v_uv);
    vec4 raw_lut = texture(t_lut, v_uv);

    vec3 correctedColor = sample_lut(sourceColor.xyz, t_lut);

    vec3 delta = abs(sourceColor.xyz - correctedColor) * 64.0;

    fragColor = vec4(mix(sourceColor.rgb, correctedColor, u_strength), 1.0);
}