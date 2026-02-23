# lab.CT_BugGroupAntPanel

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBGE_ParRef | varchar | PK |  | NO | CT_Bugs_Group Parent Reference |
| CTBGE_AnatomicalSite_DR | varchar |  | FK | SI | Anatomical Site DR |
| CTBGE_Default | varchar |  |  | SI | Default |
| CTBGE_Order | numeric |  |  | NO | Order number |
| CTBGE_Panel_DR | varchar |  | FK | SI | Panel DR |
| CTBGE_RowID | varchar |  |  | NO | - |
| CTBGE_SpecimenGroup_DR | varchar |  | FK | SI | Specimen Group DR |
| CTBGE_Specimen_DR | varchar |  | FK | SI | Specimen DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*