# TC_hmf_Manager.ErrorLog

**Schema:** TC_hmf_Manager
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFMERR_ClassMethod | varchar |  |  | NO | Class & Method |
| HMFMERR_Context | varchar |  |  | SI | Context |
| HMFMERR_SQLCODE | integer |  |  | SI | SQLCODE  |
| HMFMERR_SQLMessage | varchar |  |  | SI | SQLMSG |
| HMFMERR_Seen | bit |  |  | SI | Seen Flag |
| HMFMERR_Status | varchar |  |  | SI | Status |
| HMFMERR_UpdateDate | date |  |  | SI | Update Date |
| HMFMERR_UpdateTime | time |  |  | SI | Update Time |
| HMFMERR_UpdateUser | varchar |  |  | SI | Des Ref Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*