# SQLUser.PA_ORAnOperSecProcSnapshot

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PASPR_ParRef | bigint | PK |  | NO | PA_ORAnaestOper Parent Reference |
| PASPR_Childsub | double |  |  | NO | Childsub |
| PASPR_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| PASPR_Operation_DR | bigint |  | FK | SI | Des Ref Operation |
| PASPR_RowId | varchar |  |  | NO | - |
| PASPR_StatePPP_DR | bigint |  | FK | SI | Des Ref StatePPP |
| Q82Q1 | - |  |  | SI | Fecha Inicio Gestión |
| Q82Q2 | - |  |  | SI | Fecha Térmico Gestión |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*