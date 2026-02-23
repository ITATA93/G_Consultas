# SQLUser.PA_PersonScheduleItemOrd

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORD_ParRef | varchar | PK |  | NO | PA_PersonScheduleItem Parent Reference |
| ORD_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ORD_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| ORD_Childsub | double |  |  | NO | Childsub |
| ORD_OrdItem_DR | varchar |  | FK | SI | Des Ref OrdItem |
| ORD_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*