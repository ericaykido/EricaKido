#include <windows.h>
#include <gl/gl.h>
#include <stdio.h>
#include <gl/glu.h>
#include <gl/glext.h>
#include <math.h>

LRESULT CALLBACK WindowProc(HWND, UINT, WPARAM, LPARAM);
void EnableOpenGL(HWND hwnd, HDC*, HGLRC*);
void DisableOpenGL(HWND, HDC, HGLRC);

void face1(float xmin, float ymin, float xmax, float ymax, float n1, float z)
{
    int n = 20;
    float dx = (xmax - xmin)/(float)n;
    float dy = (ymax - ymin)/(float)n;
    float x = xmin;

    while (x <= xmax)
    {
        float y = ymin;
        while(y <= ymax)
        {
            glBegin(GL_POLYGON);
            glNormal3f(0, 0, n1);
            glVertex3f(x, y, z);
            glNormal3f(0, 0, n1);
            glVertex3f(x+dx, y, z);
            glNormal3f(0, 0, n1);
            glVertex3f(x+dx, y+dy, z);
            glNormal3f(0, 0, n1);
            glVertex3f(x, y+dy, z);
            glEnd();
            y += dy;
        }
        x += dx;
    }
}

void face2(float xmin, float zmin, float xmax, float zmax, float n1, float y)
{
    int n = 20;
    float dx = (xmax - xmin)/(float)n;
    float dz = (zmax - zmin)/(float)n;
    float x = xmin;

    while (x <= xmax)
    {
        float z = zmin;
        while(z <= zmax)
        {
            glBegin(GL_POLYGON);
            glColor3f(1,0,0);
            glNormal3f(0, n1, 0);
            glVertex3f(x, y, z);
            glNormal3f(0, n1, 0);
            glVertex3f(x+dx, y, z);
            glNormal3f(0, n1, 0);
            glVertex3f(x+dx, y, z+dz);
            glNormal3f(0, n1, 0);
            glVertex3f(x, y, z+dz);
            glEnd();
            z += dz;
        }
        x += dx;
    }
}

void face3(float ymin, float zmin, float ymax, float zmax, float n1, float x)
{
    int n = 20;
    float dy = (ymax - ymin)/(float)n;
    float dz = (zmax - zmin)/(float)n;
    float y = ymin;

    while(y <= ymax)
    {
        float z = zmin;
        while(z <= zmax)
        {
            glBegin(GL_POLYGON);
            glColor3f(1,0,0);
            glNormal3f(n1, 0, 0);
            glVertex3f(x, y, z);
            glNormal3f(n1, 0, 0);
            glVertex3f(x, y+dy, z);
            glNormal3f(n1, 0, 0);
            glVertex3f(x, y+dy, z+dz);
            glNormal3f(n1, 0, 0);
            glVertex3f(x, y, z+dz);
            glEnd();
            z += dz;
        }
        y += dy;
    }
}

void Cubo()
{
    float xmin = -0.5f;
    float ymin= -0.5f;
    float zmin = -0.5f;
    float xmax = 0.5f;
    float ymax= 0.5f;
    float zmax = 0.5f;
    face1(xmin, ymin, xmax, ymax, -1.0, -0.5f);
    face1(xmin, ymin, xmax, ymax, 1.0, 0.5f);
    face2(xmin, zmin, xmax, zmax, 1.0f, 0.5f);
    face2(xmin, zmin, xmax, zmax, -1.0f, -0.5f);
    face3(ymin, zmin, ymax, zmax, 1.0f, 0.5f);
    face3(ymin, zmin, ymax, zmax, -1.0f, -0.5f);
}

void base()
{
    glColor3f(0, 1, 0);
    face1(-2.0, -3.0, 2.0, 3.0, 1, -1.6);
}

void constroi_cadeira()
{
    glColor3f(1, 0, 0);
    glPushMatrix();
        glScalef(1.6f, 0.2f, 0.25f);
        Cubo();

        glTranslatef(0.0, 0.0, 3.625f);
        Cubo();
    glPopMatrix();

    glPushMatrix();
        glScalef(2.0f, 0.2f, 0.25f);
        glTranslatef(0.0, 9.6f, 0.0);
        Cubo();
    glPopMatrix();

    glPushMatrix();
        glScalef(2.0f, 0.25f, 1.25f);
        glTranslatef(0.0, 0.9f, 1.0f);
        Cubo();
    glPopMatrix();

    glPushMatrix();
        glScalef(0.2f, 0.2f, 1.55f);
        glTranslatef(4.5f, 0.0, -0.54f);
        Cubo();
        glTranslatef(-9.0f, 0.0, 0.0);
        Cubo();
        glTranslatef(0.0, 9.6f, 0.0);
        Cubo();
        glTranslatef(9.0f, 0.0f, 0.0);
        Cubo();
    glPopMatrix();

    glPushMatrix();
        glScalef(0.2f, 0.2f, 1.2f);
        glTranslatef(4.4f, 0.0f, 1.1f/3.0f);
        Cubo();

        glTranslatef(-8.8f, 0.0, 0.0);
        Cubo();
    glPopMatrix();

    glPushMatrix();
        glScalef(0.2f, 1.72f, 0.25f);
        glTranslatef(4.5f, 0.56f, 0.0);
        Cubo();

        glTranslatef(-9.0f, 0.0, 0.0);
        Cubo();
    glPopMatrix();

    glPushMatrix();
        glScalef(2.0f, 2.0f, 0.25f);
        glTranslatef(0.0, 0.55f, 0.8f);
        Cubo();
    glPopMatrix();
}

void Desenha_Fonte_Pontual(float p[])
{
    glDisable(GL_LIGHTING);
    glEnable(GL_POINT_SMOOTH);
    glPointSize(3);
    glColor3f(1.0, 1.0, 0.0);
    glBegin(GL_POINTS);
        glVertex3fv(p);
    glEnd();

}

void Configura_Fonte_Pontual(float p[])
{
    glEnable(GL_LIGHT0);
    glEnable(GL_LIGHTING);
    float LAP[4] = {0.0, 0.0, 0.0, 1.0};
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, LAP);

    glLightfv(GL_LIGHT0, GL_POSITION, p);

    float la[4] = {0.0, 0.0, 0.0, 0.0};
    float ld[4] = {0.8, 0.8, 0.8, 1.0};
    float ls[4] = {0.2, 0.2, 0.2, 1.0};
    glLightfv(GL_LIGHT0, GL_AMBIENT, la);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, ld);
    glLightfv(GL_LIGHT0, GL_SPECULAR, ls);

    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.1);
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.1);
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.2);

}

void Configura_Material()
{
    glEnable(GL_COLOR_MATERIAL);

    float ka[4] = {0.0, 0.0, 0.0, 1.0};
    float kd[4] = {0.8, 0.8, 0.8, 1.0};
    float ks[4] = {0.5, 0.4, 0.1, 1.0};
    float ke[4] = {0.0, 0.0, 0.0, 1.0};
    int n = 20;
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, ka);
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, kd);
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, ks);
    glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, ke);
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, n);

}

void Configura_Fonte_Refletora(float p[])
{

    glEnable(GL_LIGHT1);
    glEnable(GL_LIGHTING);

    float LAP[4] = {0.0, 0.0, 0.0, 1.0};
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, LAP);

    float d[3] = {0.0, 0.0, -1.0};
    glLightfv(GL_LIGHT1, GL_POSITION, p);
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, d);
    glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 30);
    glLightf(GL_LIGHT1, GL_SPOT_EXPONENT, 1);

    float la[4] = {0.0, 0.0, 0.0, 0.0};
    float ld[4] = {1.5, 0.8, 0.8, 1.0};
    float ls[4] = {10, 0.2, 0.2, 1.0};
    glLightfv(GL_LIGHT1, GL_AMBIENT, la);
    glLightfv(GL_LIGHT1, GL_DIFFUSE, ld);
    glLightfv(GL_LIGHT1, GL_SPECULAR, ls);

    glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, 0.1);
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.1);
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.2);

}

void Desenha_Fonte_Refletora(float p[])
{
    glDisable(GL_LIGHTING);
    glColor3f(1.0, 1.0, 0.0);
    glPushMatrix();
        glLoadIdentity();
        glTranslatef(p[0],p[1],p[2]);
        glPointSize(5);
        glEnable(GL_POINT_SMOOTH);

        glBegin(GL_POINTS);
            glVertex3f(0.0, 0.0, 0.0);
        glEnd();

        glBegin(GL_LINES);
            glVertex3f(0.0, 0.0, 0.0);
            glVertex3f(0.0, 0.0, -1.0);
        glEnd;

        float u = 0;
        float r = 0.5*tan(30*M_PI/180);
        float du = 2*M_PI/10;
        while ( u < 2*M_PI )
        {
            glBegin(GL_LINE_LOOP);
                glVertex3f(0.0, 0.0,  0.0);
                glVertex3f(r*cos(u), r*sin(u), -0.5);
                glVertex3f(r*cos(u+du), r*sin(u+du), -0.5);

            glEnd();
            u = u + du;
        }
    glPopMatrix();
}

int WINAPI WinMain(HINSTANCE hInstance,
                   HINSTANCE hPrevInstance,
                   LPSTR lpCmdLine,
                   int nCmdShow)
{
    WNDCLASSEX wcex;
    HWND hwnd;
    HDC hDC;
    HGLRC hRC;
    MSG msg;
    BOOL bQuit = FALSE;
    float theta = 0.0f;

    /* register window class */
    wcex.cbSize = sizeof(WNDCLASSEX);
    wcex.style = CS_OWNDC;
    wcex.lpfnWndProc = WindowProc;
    wcex.cbClsExtra = 0;
    wcex.cbWndExtra = 0;
    wcex.hInstance = hInstance;
    wcex.hIcon = LoadIcon(NULL, IDI_APPLICATION);
    wcex.hCursor = LoadCursor(NULL, IDC_ARROW);
    wcex.hbrBackground = (HBRUSH)GetStockObject(BLACK_BRUSH);
    wcex.lpszMenuName = NULL;
    wcex.lpszClassName = "GLSample";
    wcex.hIconSm = LoadIcon(NULL, IDI_APPLICATION);;


    if (!RegisterClassEx(&wcex))
        return 0;

    /* create main window */
    hwnd = CreateWindowEx(0,
                          "GLSample",
                          "OpenGL Sample",
                          WS_OVERLAPPEDWINDOW,
                          CW_USEDEFAULT,
                          CW_USEDEFAULT,
                          512,
                          512,
                          NULL,
                          NULL,
                          hInstance,
                          NULL);

    ShowWindow(hwnd, nCmdShow);

    /* enable OpenGL for the window */
    EnableOpenGL(hwnd, &hDC, &hRC);

    /* program main loop */
    while (!bQuit)
    {
        /* check for messages */
        if (PeekMessage(&msg, NULL, 0, 0, PM_REMOVE))
        {
            /* handle or dispatch messages */
            if (msg.message == WM_QUIT)
            {
                bQuit = TRUE;
            }
            else
            {
                TranslateMessage(&msg);
                DispatchMessage(&msg);
            }
        }
        else
        {
            glClearColor(0.0, 0.0, 0.0, 1.0);
            glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

            glMatrixMode(GL_PROJECTION);
            glLoadIdentity();
            glOrtho(-4.0, 4.0, -4.0, 4.0, -1000.0, 1000.0);
            gluLookAt(2.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0);
            glMatrixMode(GL_MODELVIEW);
            glLoadIdentity();

            glEnable(GL_NORMALIZE);
            float p[4], p1[4];
            p[0] = +3*cos(theta);
            p[1] = 0.0;
            p[2] = +3*sin(theta);
            p[3] = 1.0;

            p1[0] = 0.0;
            p1[1] = -3*sin(theta);
            p1[2] = +3*cos(theta);
            p1[3] = 1.0;

            Configura_Fonte_Pontual(p1);
            Configura_Fonte_Refletora(p);
            Configura_Material();

            base();
            constroi_cadeira();

            Desenha_Fonte_Pontual(p1);
            Desenha_Fonte_Refletora(p);

            SwapBuffers(hDC);

            theta += 0.1f;
            Sleep (100);
        }
    }

    /* shutdown OpenGL */
    DisableOpenGL(hwnd, hDC, hRC);

    /* destroy the window explicitly */
    DestroyWindow(hwnd);

    return msg.wParam;
}

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch (uMsg)
    {
    case WM_CLOSE:
        PostQuitMessage(0);
        break;

    case WM_DESTROY:
        return 0;

    case WM_KEYDOWN:
    {
        switch (wParam)
        {
        case VK_ESCAPE:
            PostQuitMessage(0);
            break;
        }
    }
    break;

    default:
        return DefWindowProc(hwnd, uMsg, wParam, lParam);
    }

    return 0;
}

void EnableOpenGL(HWND hwnd, HDC* hDC, HGLRC* hRC)
{
    PIXELFORMATDESCRIPTOR pfd;

    int iFormat;

    /* get the device context (DC) */
    *hDC = GetDC(hwnd);

    /* set the pixel format for the DC */
    ZeroMemory(&pfd, sizeof(pfd));

    pfd.nSize = sizeof(pfd);
    pfd.nVersion = 1;
    pfd.dwFlags = PFD_DRAW_TO_WINDOW |
                  PFD_SUPPORT_OPENGL | PFD_DOUBLEBUFFER;
    pfd.iPixelType = PFD_TYPE_RGBA;
    pfd.cColorBits = 24;
    pfd.cDepthBits = 16;
    pfd.iLayerType = PFD_MAIN_PLANE;

    iFormat = ChoosePixelFormat(*hDC, &pfd);

    SetPixelFormat(*hDC, iFormat, &pfd);

    /* create and enable the render context (RC) */
    *hRC = wglCreateContext(*hDC);

    wglMakeCurrent(*hDC, *hRC);
       /*
    glCullFace(GL_BACK);
    glDepthFunc(GL_LESS);

    glEnable(GL_CULL_FACE);
    glEnable(GL_DEPTH_TEST);*/
}

void DisableOpenGL (HWND hwnd, HDC hDC, HGLRC hRC)
{
    wglMakeCurrent(NULL, NULL);
    wglDeleteContext(hRC);
    ReleaseDC(hwnd, hDC);
}

