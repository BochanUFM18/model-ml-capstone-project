# Nutri Check 

## EndPoint

### Predict 

**URL**

```bash
POST /predict
```

**Body Request**
| Key   | Value            |
|-------|------------------|
| image | File gambar yang diunggah, mendukung format `.jpg`, `.png`, atau `.jpeg`. |

**Response Success**

```json
{
{
  "food_name": "Fish and Chips",
  "message": "Prediction successful",
  "status": 200
}
}
```