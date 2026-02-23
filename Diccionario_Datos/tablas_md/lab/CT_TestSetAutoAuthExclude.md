# lab.CT_TestSetAutoAuthExclude

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTSX_ParRef | varchar | PK |  | NO | CT_TestSet Parent Reference |
| CTTSX_AgeMax | double |  |  | SI | Age Max |
| CTTSX_AgeMin | double |  |  | SI | Age Min |
| CTTSX_Doctor_DR | varchar |  | FK | SI | Doctor DR |
| CTTSX_OrderNumber | numeric |  |  | NO | Order Number |
| CTTSX_RowID | varchar |  |  | NO | - |
| CTTSX_Species_DR | varchar |  | FK | SI | Species DR |
| CTTSX_TestSet_DR | varchar |  | FK | SI | Test Set DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*