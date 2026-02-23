# SQLUser.PA_ORAnaestAirwayEquipSnapshot

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAAEQ_ParRef | bigint | PK |  | NO | PA_ORAnaestSnapshot Parent Reference |
| ChildQ17DR | - |  |  | SI | Child Reference: Listado Métodos de Inducción |
| PAAEQ_ChildSub | double |  |  | NO | Childsub |
| PAAEQ_RowId | varchar |  |  | NO | - |
| PAAEQ_Type_DR | bigint |  | FK | SI | Des Ref ORCVentilationMode |
| Q12Q1 | - |  |  | SI | Tipo |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*