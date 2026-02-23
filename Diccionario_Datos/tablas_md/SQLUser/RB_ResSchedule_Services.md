# SQLUser.RB_ResSchedule_Services

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SER_ParRef | varchar | PK |  | NO | RB_ResSchedule Parent Reference |
| SER_ARCIM_ARCOS | varchar |  |  | SI | SER_ARCIM_ARCOS |
| SER_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| SER_Childsub | double |  |  | NO | Childsub |
| SER_DayOfWeek | double |  |  | SI | Day Of Week |
| SER_Desc | varchar |  |  | SI | Desc |
| SER_RBC_Service_DR | bigint |  | FK | SI | Des Ref RBC_Service |
| SER_Resource_DR | bigint |  | FK | SI | Des Ref Resource |
| SER_RowId | varchar |  |  | NO | - |
| SER_StartTime | time |  |  | SI | StartTime |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*