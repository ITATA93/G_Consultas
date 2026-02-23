# TC_hmf_Deploy_SDA3.MessageExtension

**Schema:** TC_hmf_Deploy_SDA3
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFSDAEXT_BaseMessageTriggerDR | varchar |  | FK | SI | DesRef to base trigger |
| HMFSDAEXT_Enabled | bit |  |  | SI | Enabled flag |
| HMFSDAEXT_Expression | varchar |  |  | SI | Message extension expression |
| HMFSDAEXT_InterfaceDR | varchar |  | FK | SI | DesRef to interface  |
| HMFSDAEXT_InterfaceMessageDR | varchar |  | FK | SI | DesRef to interface message |
| HMFSDAEXT_MessageDR | bigint |  | FK | SI | DesRef to message code table entry |
| HMFSDAEXT_OverrideExtensionDR | bigint |  | FK | SI | DesRef to SDA message expression override |
| HMFSDAEXT_QueryInboundInterfaceDR | varchar |  | FK | SI | DesRef to Query inbound interface for response cus... |
| HMFSDAEXT_SectionDR | bigint |  | FK | SI | DesRef to message section code table entry |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*