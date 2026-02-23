# TC_hmf_FHIR_Message.EmailRequest

**Schema:** TC_hmf_FHIR_Message
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| BCC | varchar |  |  | SI | - |
| CC | varchar |  |  | SI | - |
| Content | varchar |  |  | SI | The actual text content of the email |
| ContentType | varchar |  |  | SI | MIME type of the content in this specific part. |
| Filename | varchar |  |  | SI | A file name to attach to the email |
| From | varchar |  |  | SI | - |
| Subject | varchar |  |  | SI | - |
| To | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*