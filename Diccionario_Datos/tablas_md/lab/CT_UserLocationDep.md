# lab.CT_UserLocationDep

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTUSA_ParRef | varchar | PK |  | NO | CT_UserLocation Parent Reference |
| CTUSA_AccreditationNumber | varchar |  |  | SI | Accreditation Number |
| CTUSA_Department_DR | varchar |  | FK | NO | Department |
| CTUSA_DocCourierRun_DR | varchar |  | FK | SI | Courier Run for Doctors |
| CTUSA_Fax | varchar |  |  | SI | Fax |
| CTUSA_LocCourierRun_DR | varchar |  | FK | SI | Courier Run for Locations |
| CTUSA_Phone | varchar |  |  | SI | Phone |
| CTUSA_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*