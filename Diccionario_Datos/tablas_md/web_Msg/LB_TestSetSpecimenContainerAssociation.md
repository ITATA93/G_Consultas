# web_Msg.LB_TestSetSpecimenContainerAssociation

**Schema:** web_Msg
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| CollectionSpecimenContainers | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| LBCTestSetRevisionItem_DR | varchar |  | FK | SI | Associated LBCTestSetRevisionItems |
| LBCTestSetRevision_DR | bigint |  | FK | SI | For checking if we have enough in existing episode... |
| LBTestSetMsg_DR | varchar |  | FK | SI | Associated Test Set Msg Objects |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| SpecimenContainers | varchar |  |  | SI | Associated SpecimenContainers |
| Type | varchar |  |  | SI | Association Type 
TS: Specimen Container Collecti... |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*