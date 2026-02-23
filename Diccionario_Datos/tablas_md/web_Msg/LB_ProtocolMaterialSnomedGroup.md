# web_Msg.LB_ProtocolMaterialSnomedGroup

**Schema:** web_Msg
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBPMSG_FullySpecifiedName | varchar |  |  | SI | Fully Specified Name |
| LBPMSG_LBPMSGProtocolMaterialDR_DR | varchar |  | FK | SI | Test Set SNOMED Group
Material |
| LBPMSG_ParRef | bigint |  |  | SI | - |
| LBPMSG_RowID | varchar |  |  | SI | - |
| LBPMSG_SnomedTermDR | bigint |  | FK | SI | referance to PACSnomedTerms(SNOMED CT)  |
| LBPMSG_SpecimenContainerSnomed_DR | varchar |  | FK | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| SpecimenContainerSnomed_DR | varchar |  | FK | SI | Test Set SNOMED Group Message |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*