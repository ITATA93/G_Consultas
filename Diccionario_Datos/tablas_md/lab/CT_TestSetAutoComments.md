# lab.CT_TestSetAutoComments

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTSC_ParRef | varchar | PK |  | NO | CT_TestSet Parent Reference |
| CTTSC_Comments | varchar |  |  | SI | Comments |
| CTTSC_ConditionNo | double |  |  | NO | Condition No |
| CTTSC_Doctor_DR | varchar |  | FK | SI | Des Ref Doctor |
| CTTSC_Item_DR | varchar |  | FK | NO | Des Ref DATA Item |
| CTTSC_MaxAge | double |  |  | SI | Max Age |
| CTTSC_MinAge | double |  |  | SI | Min Age |
| CTTSC_Order | double |  |  | SI | Order |
| CTTSC_RowId | varchar |  |  | NO | - |
| CTTSC_Species_DR | varchar |  | FK | SI | Des Ref Species |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*