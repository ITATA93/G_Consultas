# SQLUser.SS_GroupLetterCategory

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LETCAT_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| LETCAT_Childsub | double |  |  | NO | Childsub |
| LETCAT_LetterCategory_DR | bigint |  | FK | SI | Des Ref DiagType |
| LETCAT_ReadAccess | varchar |  |  | SI | Read Access |
| LETCAT_RowId | varchar |  |  | NO | - |
| LETCAT_WriteAccess | varchar |  |  | SI | Write Access |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*