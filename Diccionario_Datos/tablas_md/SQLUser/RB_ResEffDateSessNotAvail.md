# SQLUser.RB_ResEffDateSessNotAvail

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NA_ParRef | varchar | PK |  | NO | RB_ResEffDateSession Parent Reference |
| NA_Childsub | double |  |  | NO | Childsub |
| NA_DateFrom | date |  |  | SI | Date From |
| NA_DateTo | double |  |  | SI | Date To |
| NA_Reason_DR | bigint |  | FK | SI | Des Ref Reason not avail |
| NA_Remarks | varchar |  |  | SI | Remarks |
| NA_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*