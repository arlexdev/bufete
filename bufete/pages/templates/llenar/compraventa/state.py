import reflex as rx
#from bufete.models import Contract
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import tempfile
import stripe
#from bufete.auth.state import AuthState

# Configurar la clave secreta de Stripe
stripe.api_key = ""

class ContractState():
    """Estado para el formulario de contratos."""

    # Variables para Stripe
    payment_status: str = ""
    session_id: str = ""
    payment_completed: bool = False

    pdf_content: str = ""

    # Control del formulario por pasos
    current_step: int = 1
    total_steps: int = 3
    progress_value: int = 0

    # Datos básicos
    uso: str = ""
    nombre: str = ""
    ci: str = ""

    # Datos del inmueble
    tipo_inmueble: str = ""
    partida: str = ""
    nro_oficina: str = ""
    piso: str = ""

    # Datos del parqueo
    partida_parqueo: str = ""

    # Ubicación
    edificio: str = ""
    calle: str = ""
    zona: str = ""
    ciudad: str = ""

    # Estado del formulario
    form_data: dict = {}
    contract_preview: str = ""

    # Campo activo para resaltado
    campo_activo: str = ""

    @rx.var(cache=True)
    def step_valid(self) -> bool:
        if self.current_step == 1:
            return bool(self.uso and self.nombre and self.ci)
        elif self.current_step == 2:
            return bool(self.tipo_inmueble and self.partida)
        elif self.current_step == 3:
            return bool(self.edificio and self.calle)
        return False

    @rx.event
    def next_step(self):
        if self.current_step < self.total_steps:
            self.current_step += 1
            self.update_progress()

    @rx.event
    def previous_step(self):
        if self.current_step > 1:
            self.current_step -= 1
            self.update_progress()

    def update_progress(self):
        self.progress_value = (self.current_step - 1) * (100 // (self.total_steps - 1))

    @rx.event
    def establecer_campo_activo(self, campo: str):
        """Establece el campo activo para el resaltado."""
        self.campo_activo = campo

    @rx.event
    def set_uso(self, value: str):
        self.uso = value
        self.update_preview()

    @rx.event
    def set_nombre(self, value: str):
        self.nombre = value
        self.update_preview()

    @rx.event
    def set_ci(self, value: str):
        self.ci = value
        self.update_preview()

    @rx.event
    def set_tipo_inmueble(self, value: str):
        self.tipo_inmueble = value
        self.update_preview()

    @rx.event
    def set_partida(self, value: str):
        self.partida = value
        self.update_preview()

    @rx.event
    def set_nro_oficina(self, value: str):
        self.nro_oficina = value
        self.update_preview()

    @rx.event
    def set_piso(self, value: str):
        self.piso = value
        self.update_preview()

    @rx.event
    def set_partida_parqueo(self, value: str):
        self.partida_parqueo = value
        self.update_preview()

    @rx.event
    def set_edificio(self, value: str):
        self.edificio = value
        self.update_preview()

    @rx.event
    def set_calle(self, value: str):
        self.calle = value
        self.update_preview()

    @rx.event
    def set_zona(self, value: str):
        self.zona = value
        self.update_preview()

    @rx.event
    def set_ciudad(self, value: str):
        self.ciudad = value
        self.update_preview()

    def update_preview(self):
        """Actualiza la vista previa del contrato."""
        self.contract_preview = f"""
        SEÑOR NOTARIO DE FE PÚBLICA

        En los registros de escrituras públicas a su cargo, sírvase insertar un contrato de
        arrendamiento de inmueble para uso {self.uso} (comercial/vivienda),
        de acuerdo a las siguientes clausulas y condiciones:

        PRIMERA (DE LAS PARTES).–
        Dirá Ud. que intervienen en la celebración del presente Contrato las siguientes personas:

        1.1.- El señor {self.nombre} con Carnet de Identidad {self.ci},
        mayor de edad y hábil por ley, propietario del inmueble {self.tipo_inmueble}
        (oficina/casa/departamento) con partida en Derechos Reales {self.partida}
        signada como Oficina {self.nro_oficina} del piso {self.piso}
        y del Parqueo con partida en derechos Reales N° {self.partida_parqueo}
        del Edificio {self.edificio} ubicado en la calle {self.calle}
        de la Zona {self.zona} de la ciudad de {self.ciudad},
        quien en adelante se denominará "ARRENDADOR".
        """

    @rx.event
    def handle_submit(self, form_data: dict):
        """Maneja el envío final del formulario."""
        self.form_data = form_data
        for key, value in form_data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.update_preview()
        self.progress_value = 100

    @rx.var(cache=True)
    def is_last_step(self) -> bool:
        return self.current_step == self.total_steps

    @rx.var(cache=True)
    def form_completed(self) -> bool:
        if self.current_step == self.total_steps:
            return bool(self.edificio and self.calle and self.zona and self.ciudad)
        return False

    @rx.event
    def finish_contract(self):
        self.progress_value = 100
        return rx.toast.success("¡Contrato completado con éxito!")

    @rx.event
    async def generar_pdf(self):
        try:
            # Crear archivo temporal en memoria
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')

            # Crear el PDF
            c = canvas.Canvas(temp_file.name, pagesize=letter)

            # Configurar fuente y tamaño
            c.setFont("Helvetica-Bold", 14)
            y = 800

            # Título
            c.drawString(100, y, "SEÑOR NOTARIO DE FE PÚBLICA")
            y -= 30

            # Cambiar a fuente normal
            c.setFont("Helvetica", 12)

            # Contenido del contrato
            contenido = [
                "SEÑOR NOTARIO DE FE PÚBLICA",
                f"En los registros de escrituras públicas a su cargo, sírvase insertar un contrato de",
                f"arrendamiento de inmueble para uso {self.uso} (comercial/vivienda),",
                f"de acuerdo a las siguientes clausulas y condiciones:",
                "",
                "PRIMERA (DE LAS PARTES).–",
                "Dirá Ud. que intervienen en la celebración del presente Contrato las siguientes personas:",
                "",
                f"1.1.- El señor {self.nombre} con Carnet de Identidad {self.ci},",
                f"mayor de edad y hábil por ley, propietario del inmueble {self.tipo_inmueble}",
                f"(oficina/casa/departamento) con partida en Derechos Reales {self.partida}",
                f"signada como Oficina {self.nro_oficina} del piso {self.piso}",
                f"y del Parqueo con partida en derechos Reales N° {self.partida_parqueo}",
                f"del Edificio {self.edificio} ubicado en la calle {self.calle}",
                f"de la Zona {self.zona} de la ciudad de {self.ciudad},",
                "quien en adelante se denominará ARRENDADOR."
            ]

            for linea in contenido:
                c.drawString(100, y, linea)
                y -= 20

            c.save()
            temp_file.close()

            # Leer el archivo como bytes
            with open(temp_file.name, 'rb') as file:
                pdf_bytes = file.read()

            # Eliminar archivo temporal
            os.unlink(temp_file.name)

            # Retornar el evento de descarga usando data en lugar de url
            return rx.download(
                data=pdf_bytes,
                filename="contrato.pdf"
            )

        except Exception as e:
            return rx.toast.error(f"Error al generar PDF: {str(e)}")


    @rx.event
    async def create_checkout_session(self):
        try:
            if not self.is_authenticated:
                return rx.toast.error("Debes iniciar sesión para realizar el pago")

            print(f"User ID antes de crear sesión: {self.user_id}")
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Contrato de Arrendamiento',
                        },
                        'unit_amount': 1000,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=f'http://localhost:3000/success?session_id={{CHECKOUT_SESSION_ID}}&user_id={self.user_id}',
                cancel_url='http://localhost:3000/cancel',
                metadata={'user_id': str(self.user_id)}
            )

            self.session_id = checkout_session.id
            print(f"Session ID creado: {self.session_id}")
            return rx.redirect(checkout_session.url)
        except Exception as e:
            print(f"Error en create_checkout_session: {str(e)}")
            return rx.toast.error(f"Error al crear sesión de pago: {str(e)}")


    @rx.event
    async def verify_payment(self):
        try:
            print("Inicio de verify_payment")
            session_id = self.router.page.params.get("session_id")
            print(f"Session ID: {session_id}")

            if not session_id:
                return rx.toast.error("No se encontró el ID de la sesión")

            session = stripe.checkout.Session.retrieve(session_id)
            print(f"Estado del pago: {session.payment_status}")

            if session.payment_status == "paid":
                if not self.is_authenticated:
                    return rx.toast.error("Usuario no autenticado")

                print(f"Usuario autenticado: {self.is_authenticated}")
                print(f"User ID: {self.user_id}")

                with rx.session() as db_session:
                    try:
                        nuevo_contrato = Contract(
                            fecha=datetime.now().strftime("%Y-%m-%d"),
                            documento="Acuerdos de compra de bienes raíces",
                            estado="PAGADO",
                            user_id=self.user_id
                        )
                        print(f"Creando contrato con user_id: {self.user_id}")
                        db_session.add(nuevo_contrato)
                        db_session.commit()
                        print("Contrato guardado exitosamente")

                    except Exception as db_error:
                        print(f"Error al guardar en la base de datos: {str(db_error)}")
                        raise db_error

                return await self.generar_pdf()
            else:
                self.payment_status = "pending"
                return rx.toast.info("El pago está pendiente")

        except Exception as e:
            print(f"Error en verify_payment: {str(e)}")
            return rx.toast.error(f"Error al verificar el pago: {str(e)}")
