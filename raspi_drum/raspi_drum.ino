int data = 0;

void setup()
{
    Serial.begin(115200);

    pinMode(2, INPUT_PULLUP);
    pinMode(3, INPUT_PULLUP);
    pinMode(4, INPUT_PULLUP);
    pinMode(5, INPUT_PULLUP);
}

void loop()
{
    data = 0;

    if (!digitalRead(2))
        data += 1;
    if (!digitalRead(3))
        data += 2;
    if (!digitalRead(4))
        data += 4;
    if (!digitalRead(5))
        data += 8;
        

    Serial.write(data);
}