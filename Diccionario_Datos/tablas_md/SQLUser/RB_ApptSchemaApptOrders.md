# SQLUser.RB_ApptSchemaApptOrders

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORD_ParRef | varchar | PK |  | NO | RB_ApptSchemaAppt Parent Reference |
| ORD_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ORD_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| ORD_Childsub | double |  |  | NO | Childsub |
| ORD_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*