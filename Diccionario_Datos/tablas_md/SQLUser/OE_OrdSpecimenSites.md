# SQLUser.OE_OrdSpecimenSites

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SITE_ParRef | varchar | PK |  | NO | OE_OrdSpecimen Parent Reference |
| ChildQ24DR | - |  |  | SI | Child Reference: Superficial Sensation |
| Q23Q1 | - |  |  | SI | Reflex |
| Q23Q2 | - |  |  | SI | Left |
| Q23Q3 | - |  |  | SI | Right |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SITE_Childsub | double |  |  | NO | Childsub |
| SITE_Code | varchar |  |  | SI | Code |
| SITE_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*