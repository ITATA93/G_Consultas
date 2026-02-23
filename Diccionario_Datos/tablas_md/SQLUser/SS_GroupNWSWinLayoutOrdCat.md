# SQLUser.SS_GroupNWSWinLayoutOrdCat

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CAT_ParRef | varchar | PK |  | NO | SS_GroupNWS_WindowLayout Parent Reference |
| CAT_Childsub | double |  |  | NO | Childsub |
| CAT_OrdCat_DR | bigint |  | FK | SI | Des Ref OrdCat |
| CAT_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*