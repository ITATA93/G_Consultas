# lab.CT_TestSetContainers

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTSY_ParRef | varchar | PK |  | NO | CT_TestSet Parent Reference |
| CTTSY_Comment | varchar |  |  | SI | Comment |
| CTTSY_Container_DR | varchar |  | FK | NO | Container DR |
| CTTSY_MinVolume | double |  |  | SI | Min Volume |
| CTTSY_Order | double |  |  | SI | Order number |
| CTTSY_RowID | varchar |  |  | NO | - |
| CTTSY_Specimen_DR | varchar |  | FK | NO | Specimen DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*