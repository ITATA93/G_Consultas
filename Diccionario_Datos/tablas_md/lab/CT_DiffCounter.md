# lab.CT_DiffCounter

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDIF_RowId | bigint | PK |  | NO | - |
| CTDIF_IncludeInCalculation | varchar |  |  | SI | Include in calculation |
| CTDIF_Key | varchar |  |  | SI | Key |
| CTDIF_SEQUENCE | double |  |  | SI | Display sequence |
| CTDIF_TestCode_DR | varchar |  | FK | SI | Des Ref TestCode |
| CTDIF_TestSet_DR | varchar |  | FK | SI | Des Ref Test Set |
| CTDIF_TotalCounter | varchar |  |  | SI | Total Counter |
| CTDIF_User_DR | varchar |  | FK | SI | Des Ref User |
| CTDIF_WCC_DR | varchar |  | FK | SI | White Cell Counter DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*