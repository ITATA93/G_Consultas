# lab.CT_BugsAntiBioticPanel

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBUP_ParRef | varchar | PK |  | NO | CT_Bugs Parent Reference |
| CTBUP_AnatomicalSite_DR | varchar |  | FK | SI | Anatomical Site DR |
| CTBUP_Default | varchar |  |  | SI | Default |
| CTBUP_Order | numeric |  |  | NO | Order number |
| CTBUP_Panel_DR | varchar |  | FK | SI | Panel DR |
| CTBUP_RowID | varchar |  |  | NO | - |
| CTBUP_Specimen_DR | varchar |  | FK | SI | Specimen DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*