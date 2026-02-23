# lab.CT_TestCodeContainers

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTCB_ParRef | varchar | PK |  | NO | CT_TestCode Parent Reference |
| CTTCB_Comment | varchar |  |  | SI | Comment |
| CTTCB_Container_DR | varchar |  | FK | NO | Container DR |
| CTTCB_MinVolume | double |  |  | SI | Min Volume |
| CTTCB_Order | double |  |  | SI | Order |
| CTTCB_RowID | varchar |  |  | NO | - |
| CTTCB_Specimen_DR | varchar |  | FK | NO | Specimen DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*