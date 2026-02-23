# SQLUser.PA_ORAnOpPosEquipSnapshot

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAPOSEQ_ParRef | varchar | PK |  | NO | PA_ORAnOperPositionSnapshot Parent Reference |
| ChildQ07DR | - |  |  | SI | Child Reference: CABEZA Y CARA |
| PAPOSEQ_Childsub | double |  |  | NO | Childsub |
| PAPOSEQ_RowId | varchar |  |  | NO | - |
| PAPOSEQ_Type_DR | bigint |  | FK | SI | Des Ref PACAnalgetics |
| Q24Q1 | - |  |  | SI | Ubicación |
| Q24Q2 | - |  |  | SI | Ubicación Otro |
| Q24Q3 | - |  |  | SI | Lateralidad |
| Q24Q4 | - |  |  | SI | Evaluación de la piel |
| Q24Q5 | - |  |  | SI | Tipo de Lesión |
| Q24Q6 | - |  |  | SI | Signos de Alarma |
| Q24Q7 | - |  |  | SI | Signos de Alarma Otro |
| Q24Q8 | - |  |  | SI | Tipo de Dispositivo Médico |
| Q24Q9 | - |  |  | SI | Tipo de Dispositivo Médico Otro |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*