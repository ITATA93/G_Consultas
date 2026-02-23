# SQLUser.PA_ORAnaestInductionTechSnapshot

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAIND_ParRef | bigint | PK |  | NO | PA_ORAnaestSnapshot Parent Reference |
| PAIND_ChildSub | double |  |  | NO | Childsub |
| PAIND_RowId | varchar |  |  | NO | - |
| PAIND_Type_DR | bigint |  | FK | SI | Des Ref MRCCareEventType |
| Q185Q1 | - |  |  | SI | Tratamiento |
| Q185Q2 | - |  |  | SI | Fecha de Inicio |
| Q185Q3 | - |  |  | SI | Fecha de Termino |
| Q185Q4 | - |  |  | SI | Esquema / Tipo / Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*