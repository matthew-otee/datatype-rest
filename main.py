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

@app.get("/intbool")
def read_intbool():
        return {
            "BOOL0": False,
            "BOOL1": False,
            "BOOL2": False,
            "BOOL3": False,
            "BOOL4": False,
            "BOOL5": False,
            "BOOL6": False,
            "BOOL7": False,
            "INT0": 10,
            "INT1": 21,
            "INT2": 31,
            "INT3": 41,
            "INT4": 51,
            "INT5": 61,
            "INT6": 71,
            "INT7": 81
        }

@app.get("/bool")
def read_bool():
    return {
        "BOOL0": False,
        "BOOL1": False,
        "BOOL2": False,
        "BOOL3": False,
        "BOOL4": False,
        "BOOL5": False,
        "BOOL6": False,
        "BOOL7": False,
        "BOOL8": False,
        "BOOL9": False,
        "BOOL10": False,
        "BOOL11": False,
        "BOOL12": False,
        "BOOL13": False,
        "BOOL14": False,
        "BOOL15": False,
        "BOOL16": False,
        "BOOL17": False,
        "BOOL18": False,
        "BOOL19": False,
        "BOOL20": False,
        "BOOL21": False,
        "BOOL22": False,
        "BOOL23": False,
        "BOOL24": False
    }

if __name__ == "__main__":
    main()

