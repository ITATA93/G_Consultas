# lab.CT_TestCodeAccNo

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTCAN_ParRef | varchar | PK |  | NO | CT_TestCode Parent Reference |
| CTTCAN_AccreditationNumber | varchar |  |  | SI | Accreditation Number |
| CTTCAN_EndDate | date |  |  | SI | End Date |
| CTTCAN_MethodDR | varchar |  | FK | SI | Method DR |
| CTTCAN_RowID | varchar |  |  | NO | - |
| CTTCAN_Sequence | numeric |  |  | NO | Sequence |
| CTTCAN_StartDate | date |  |  | SI | Start Date |
| CTTCAN_UserSites | varchar |  |  | SI | User Sites (comma seperated) |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*