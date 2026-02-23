# web_Msg.LB_QCRuleException

**Schema:** web_Msg
**Columnas:** 45
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBQCRE_10xAction | varchar |  |  | SI | 10x Action
StandardType: LabQCRuleAction |
| LBQCRE_10xSequenceNumber | numeric |  |  | SI | 10x Sequence Number |
| LBQCRE_12sAction | varchar |  |  | SI | 12s Action
StandardType: LabQCRuleAction |
| LBQCRE_12sSequenceNumber | numeric |  |  | SI | 12s Sequence Number |
| LBQCRE_12xAction | varchar |  |  | SI | 12x Action
StandardType: LabQCRuleAction |
| LBQCRE_12xSequenceNumber | numeric |  |  | SI | 12x Sequence Number |
| LBQCRE_13sAction | varchar |  |  | SI | 13s Action
StandardType: LabQCRuleAction |
| LBQCRE_13sSequenceNumber | numeric |  |  | SI | 13s Sequence Number |
| LBQCRE_22sAction | varchar |  |  | SI | 22s Action
StandardType: LabQCRuleAction |
| LBQCRE_22sSequenceNumber | numeric |  |  | SI | 22s Sequence Number |
| LBQCRE_2of32sAction | varchar |  |  | SI | 2of32s Action
StandardType: LabQCRuleAction |
| LBQCRE_2of32sSequenceNumber | numeric |  |  | SI | 2of32s Sequence Number |
| LBQCRE_31sAction | varchar |  |  | SI | 31s Action
StandardType: LabQCRuleAction |
| LBQCRE_31sSequenceNumber | numeric |  |  | SI | 31s Sequence Number |
| LBQCRE_41sAction | varchar |  |  | SI | 41s Action
StandardType: LabQCRuleAction |
| LBQCRE_41sSequenceNumber | numeric |  |  | SI | 41s Sequence Number |
| LBQCRE_6xAction | varchar |  |  | SI | 6x Action
StandardType: LabQCRuleAction |
| LBQCRE_6xSequenceNumber | numeric |  |  | SI | 6x Sequence Number |
| LBQCRE_7TAction | varchar |  |  | SI | 7T Action
StandardType: LabQCRuleAction |
| LBQCRE_7TSequenceNumber | numeric |  |  | SI | 7T Sequence Number |
| LBQCRE_8xAction | varchar |  |  | SI | 8x Action
StandardType: LabQCRuleAction |
| LBQCRE_8xSequenceNumber | numeric |  |  | SI | 8x Sequence Number |
| LBQCRE_9xAction | varchar |  |  | SI | 9x Action
StandardType: LabQCRuleAction |
| LBQCRE_9xSequenceNumber | numeric |  |  | SI | 9x Sequence Number |
| LBQCRE_ExceptionLevel | varchar |  |  | SI | Level of exception
StandardType: LBQCRuleExceptio... |
| LBQCRE_LastUpdateDate | date |  |  | SI | Last update date |
| LBQCRE_LastUpdateTime | time |  |  | SI | Last update time |
| LBQCRE_LastUpdateUser | bigint |  |  | SI | Last update user |
| LBQCRE_NNAction | varchar |  |  | SI | NN Action
StandardType: LabQCRuleAction |
| LBQCRE_NNSequenceNumber | numeric |  |  | SI | NN Sequence Number |
| LBQCRE_QCBatchLevel_DR | varchar |  | FK | SI | Link to the Batch Level |
| LBQCRE_QCScheme_DR | bigint |  | FK | SI | Link to the QC Scheme |
| LBQCRE_QCTestItem_DR | varchar |  | FK | SI | Link to the Value Group |
| LBQCRE_QCValueGroup_DR | varchar |  | FK | SI | Link to the Value Group |
| LBQCRE_R4sAction | varchar |  |  | SI | R4s Action
StandardType: LabQCRuleAction |
| LBQCRE_R4sSequenceNumber | numeric |  |  | SI | R4s Sequence Number |
| LBQCRE_RowID | varchar |  |  | SI | - |
| LBQCRE_TRAction | varchar |  |  | SI | TR Action
StandardType: LabQCRuleAction |
| LBQCRE_TRSequenceNumber | numeric |  |  | SI | TR Sequence Number |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*