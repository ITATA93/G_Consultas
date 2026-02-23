# Region_CLXX_Integration_HS_Log.ReLoadDoc

**Schema:** Region_CLXX_Integration_HS_Log
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Integración Health Share**. Conexión con sistema de interoperabilidad.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| DocumentDate | date |  |  | SI | - |
| DocumentId | varchar |  |  | SI | - |
| DocumentTime | time |  |  | SI | - |
| DocumentType | varchar |  |  | SI | - |
| InitDateTime | timestamp |  |  | SI | - |
| PAAdmId | varchar |  |  | SI | - |
| PatientId | varchar |  |  | SI | - |
| Priority | varchar |  |  | SI | - |
| SendDateTime | timestamp |  |  | SI | - |
| TypeDate | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*