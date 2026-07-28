import uvicorn
from fastapi import FastAPI

app = FastAPI(title="My Pyproject App")

def main():
    print("Hello from rest-test!")
    uvicorn.run(app, host="0.0.0.0", port=8001)


@app.get("/")
def read_root():
    return {
        "BOOL":   True,
        "BYTE":   255,
        "DATE":   "2026-07-28",
        "DINT":   -2147483648,
        "DT":     "2026-07-28T14:23:05",
        "DWORD":  4294967295,
        "INT":    -32768,
        "LINT":   -9223372036854775808,
        "LWORD":  18446744073709551615,
        "SINT":   -128,
        "STRING": "IEC62443_TEST_STRING",
        "TIME":   "PT1H2M3.500S",
        "TOD":    "14:23:05.500",
        "UDINT":  4294967295,
        "UINT":   65535,
        "ULINT":  18446744073709551615,
        "USINT":  255,
        "WORD":   65535
    }

if __name__ == "__main__":
    main()

