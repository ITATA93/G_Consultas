# SQLUser.PA_ORAnOpBiopGastSnapshot

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAOPBG_ParRef | bigint | PK |  | NO | PA_ORAnaestOperation Parent Reference |
| ChildQ15DR | - |  |  | SI | Child Reference: TÓRAX y ABDOMEN |
| PAOPBG_Childsub | double |  |  | NO | Childsub |
| PAOPBG_RowId | varchar |  |  | NO | - |
| PAOPBG_Type_DR | bigint |  | FK | SI | Des Ref StatePPP |
| Q12Q1 | - |  |  | SI | Ubicación |
| Q12Q2 | - |  |  | SI | Ubicación Otro |
| Q12Q3 | - |  |  | SI | Lateralidad |
| Q12Q4 | - |  |  | SI | Evaluación de la piel |
| Q12Q5 | - |  |  | SI | Tipo de Lesión |
| Q12Q6 | - |  |  | SI | Signos de Alarma |
| Q12Q7 | - |  |  | SI | Signos de Alarma Otro |
| Q12Q8 | - |  |  | SI | Tipo de Dispositivo Médico |
| Q12Q9 | - |  |  | SI | Tipo de Dispositivo Médico Otro |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*