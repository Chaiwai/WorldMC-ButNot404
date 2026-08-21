#version 150

precision highp float;








#define hue(v)  ((.6+.6*cos(6.*(v)+vec4(0, 23, 21, 1)))+vec4(0., 0., 0., 1.) )

#define finalize() { \
    vertexDistance=length((ModelViewMat*vertex).xyz); \
    texCoord0=UV0; \
}

in vec3 Position;
in vec4 Color;
in vec2 UV0;
in ivec2 UV2;


uniform sampler2D Sampler0;

uniform sampler2D Sampler2;

uniform mat4 ModelViewMat;
uniform mat4 ProjMat;

uniform float GameTime;

out float vertexDistance;
out vec4 vertexColor;
out vec2 texCoord0;

void f_b16b5970(inout vec4 vertex) {
    gl_Position=ProjMat*ModelViewMat*vertex;
}

void f_4ded4dee() {
    vertexColor=Color*texelFetch(Sampler2, UV2 / 16, 0);
}


void f_ecce68a5(inout vec4 vertex) {
    f_b16b5970(vertex);
    if(Position.z==0. && gl_Position.x > .95) {
        vertexColor=vec4(0);
    }else{
        f_4ded4dee();
    }
    finalize();
}



void f_1d7b9011() {
    vertexColor=hue(gl_Position.x+GameTime*1000.)*texelFetch(Sampler2, UV2 / 16, 0);
}

void f_9d684761() {
    gl_Position.y+=sin(GameTime*12000.+(gl_Position.x*6)) / 150.;
}

void f_c65a399e(inout vec4 vertex) {
    f_b16b5970(vertex);
    f_1d7b9011();
    finalize();
}

void f_689aeba7(inout vec4 vertex) {
    f_b16b5970(vertex);
    f_4ded4dee();
    f_9d684761();
    finalize();
}

void f_f0fdefb9(inout vec4 vertex) {
    f_b16b5970(vertex);
    f_9d684761();
    f_1d7b9011();
    finalize();
}

void f_4c96e974(inout vec4 vertex) {
    f_4ded4dee();
    float vertexId=mod(gl_VertexID, 4.);
    if(vertex.z <= 0.) {
        if(vertexId==3. || vertexId==0.) {
            vertex.y+=cos(GameTime*12000. / 4)*.1;
            vertex.y+=max(cos(GameTime*12000. / 4)*.1, 0.);
        }
    }else{
        if(vertexId==3. || vertexId==0.) {
            vertex.y-=cos(GameTime*12000. / 4)*3;
            vertex.y-=max(cos(GameTime*12000. / 4)*4, 0.);
        }
    }
    f_b16b5970(vertex);
    finalize();
}

void f_ddb313ab(inout vec4 vertex) {
    float vertexId=mod(gl_VertexID, 4.);
    if(vertex.z <= 0.) {
        if(vertexId==3. || vertexId==0.) {
            vertex.y+=cos(GameTime*12000. / 4)*.1;
            vertex.y+=max(cos(GameTime*12000. / 4)*.1, 0.);
        }
    }else{
        if(vertexId==3. || vertexId==0.) {
            vertex.y-=cos(GameTime*12000. / 4)*3;
            vertex.y-=max(cos(GameTime*12000. / 4)*4, 0.);
        }
    }
    f_1d7b9011();
    f_b16b5970(vertex);
    finalize();
}

void f_776d9eaf(inout vec4 vertex, float speed) {
    f_b16b5970(vertex);
    float blink=abs(sin(GameTime*12000.*speed));
    vertexColor=Color*blink*texelFetch(Sampler2, UV2 / 16, 0);
    finalize();
}



void f_3fd85f31(inout vec4 vertex) {
    f_b16b5970(vertex);
    f_4ded4dee();
    vertexColor=vec4(1, 1, 1, vertexColor.a); 
    finalize();
}


void main() {
    vec4 vertex=vec4(Position, 1.);
    ivec3 iColor=ivec3(Color.xyz*255+vec3(.5));

    
    
    if(iColor==ivec3(255, 85, 85))
    {
        f_ecce68a5(vertex);
        return;
    }
    

    
    if(fract(Position.z) < .1) {
        
        
        if(iColor==ivec3(19, 23, 9))
        {
            gl_Position=vec4(2, 2, 2, 1);
            f_4ded4dee();
            finalize();
            return;
        }
        

        
        
        if(iColor==ivec3(57, 63, 63)) {
            
            
            f_b16b5970(vertex);
            f_4ded4dee();
            finalize();
            return;
        }

        
        if(iColor==ivec3(57, 63, 62)) {
            f_689aeba7(vertex);
            return;
        }

        
        if(iColor==ivec3(57, 62, 63)) {
            
            f_689aeba7(vertex);
            return;
        }

        
        if(iColor==ivec3(57, 62, 62)) {
            f_4c96e974(vertex);
            return;
        }

        
        if(iColor==ivec3(57, 61, 63)) {
            f_4c96e974(vertex);
            return;
        }

        
        if(iColor==ivec3(57, 61, 62)) {
            f_776d9eaf(vertex, .5);
            return;
        }

        

        
    }

    
    
    if(iColor==ivec3(78, 92, 36))
    {
        f_3fd85f31(vertex);
        return;
    }
    

    
    
    
    if(iColor==ivec3(230, 255, 254))
    {
        f_c65a399e(vertex);
        return;
    }

    
    if(iColor==ivec3(230, 255, 250))
    {
        f_689aeba7(vertex);
        return;
    }

    
    if(iColor==ivec3(230, 251, 254))
    {
        f_f0fdefb9(vertex);
        return;
    }

    
    if(iColor==ivec3(230, 251, 250))
    {
        f_4c96e974(vertex);
        return;
    }

    
    if(iColor==ivec3(230, 247, 254))
    {
        f_ddb313ab(vertex);
        return;
    }

    
    if(iColor==ivec3(230, 247, 250))
    {
        f_776d9eaf(vertex, .5);
        return;
    }

    
    

    
    
    
    if(iColor==ivec3(255, 255, 254))
    {
        f_c65a399e(vertex);
        return;
    }

    
    if(iColor==ivec3(255, 255, 253))
    {
        f_689aeba7(vertex);
        return;
    }

    
    if(iColor==ivec3(255, 255, 25))
    {
        f_f0fdefb9(vertex);
        return;
    }

    
    if(iColor==ivec3(255, 255, 251))
    {
        f_4c96e974(vertex);
        return;
    }

    
    if(iColor==ivec3(255, 254, 254))
    {
        f_ddb313ab(vertex);
        return;
    }
    

    
    f_b16b5970(vertex);
    f_4ded4dee();
    finalize();
}