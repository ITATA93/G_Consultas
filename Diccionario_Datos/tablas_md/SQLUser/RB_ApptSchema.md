# SQLUser.RB_ApptSchema

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SCH_RowId | bigint | PK |  | NO | - |
| SCH_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| SCH_Code | varchar |  |  | NO | Code |
| SCH_DateFrom | date |  |  | SI | DateFrom |
| SCH_DateTo | date |  |  | SI | DateTo |
| SCH_Desc | varchar |  |  | NO | Description |
| SCH_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| SCH_NumberOfAppt | double |  |  | SI | Number Of Appt |
| SCH_Type | varchar |  |  | SI | Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*