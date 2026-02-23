# SQLUser.RB_ResEffDateSessPayorRestr

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RESTR_ParRef | varchar | PK |  | NO | RB_ResEffDateSession Parent Reference |
| RESTR_Childsub | double |  |  | NO | Childsub |
| RESTR_DateFrom | date |  |  | SI | DateFrom |
| RESTR_DateTo | date |  |  | SI | DateTo |
| RESTR_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| RESTR_NFMIDep_DR | varchar |  | FK | SI | Des Ref NFMIDep |
| RESTR_RestrReason_DR | bigint |  | FK | SI | Des Ref RestrReason |
| RESTR_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*