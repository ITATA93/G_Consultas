# TC_hmf_Adapter.InterfaceMessage

**Schema:** TC_hmf_Adapter
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HMFADAPMSG_ParRef | varchar | PK |  | NO | Interface Parent Reference |
| HMFADAPINT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HMFADAPINT_System | varchar |  |  | SI | System |
| HMFADAPMSG_DateFrom | date |  |  | SI | Date From |
| HMFADAPMSG_DateTo | date |  |  | SI | Date To |
| HMFADAPMSG_Enabled | bit |  |  | SI | Enabled flag |
| HMFADAPMSG_MessageDR | bigint |  | FK | SI | DesRef to message code table entry |
| HMFADAPMSG_TransformDR | bigint |  | FK | SI | DesRef to message transformation code table entry |
| ID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*