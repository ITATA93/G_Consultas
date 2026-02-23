# lab.CT_DynamicFunctionLayout

**Schema:** lab
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDFL_ParRef | varchar | PK |  | NO | CT_DynamicFunction Parent Reference |
| CTDFL_FieldColumn | double |  |  | SI | Field Column |
| CTDFL_FieldRow | double |  |  | SI | Field Row |
| CTDFL_LabelFormat | varchar |  |  | SI | Label Format |
| CTDFL_LabelName | varchar |  |  | SI | Label Name |
| CTDFL_LengthField | double |  |  | SI | Field Length |
| CTDFL_LengthRefRanges | double |  |  | SI | Length Ref Ranges |
| CTDFL_LengthUnits | double |  |  | SI | Units Length |
| CTDFL_NameRR | varchar |  |  | SI | Name RR |
| CTDFL_NameResult | varchar |  |  | SI | Name Result |
| CTDFL_NameUnits | varchar |  |  | SI | Name Units |
| CTDFL_RowID | varchar |  |  | NO | - |
| CTDFL_Sequence | double |  |  | NO | Sequence |
| CTDFL_TestItem_DR | varchar |  | FK | SI | Test Item DR |
| CTDFL_Type | varchar |  |  | SI | Field Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*