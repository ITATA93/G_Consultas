# SQLUser.SS_ProfileLetterCategory

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LC_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| LC_LetterCategory_DR | bigint |  | FK | SI | Des Ref DiagType |
| LC_ReadAccess | varchar |  |  | SI | Read Access |
| LC_RowID | varchar |  |  | NO | - |
| LC_WriteAccess | varchar |  |  | SI | Write Access |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*