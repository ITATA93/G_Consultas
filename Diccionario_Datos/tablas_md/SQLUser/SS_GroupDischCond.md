# SQLUser.SS_GroupDischCond

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DC_ParREf | bigint | PK |  | NO | SS_Group Parent Reference |
| DC_Childsub | double |  |  | NO | Childsub |
| DC_DischCond_DR | bigint |  | FK | SI | Des Ref DischCond |
| DC_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*